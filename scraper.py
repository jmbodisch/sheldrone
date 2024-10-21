import mysql.connector.cursor
import requests, json, mysql.connector, os
from dotenv import load_dotenv
import splatnet3_scraper.auth
import splatnet3_scraper.auth.tokens
import constants
import time

def login(nso: splatnet3_scraper.auth.NSO, uri: str, uid: str):
    """Generates a session token based on the given Nintendo Online URI."""
    try:
        sesh_code = nso.parse_npf_uri(uri)
        print(sesh_code)
        SESSION_TOKEN = nso.get_session_token(sesh_code) 
        print("session token successfully generated: ")
        print(SESSION_TOKEN)
        insert_tokens(uid=uid, session_token=splatnet3_scraper.auth.Token(SESSION_TOKEN, "session_token", time.time()))
        return "Successfully added user and token to database!"
    except:
        return "An error occurred."

def insert_tokens(uid: str, db: mysql.connector.MySQLConnection | None=None, session_token: splatnet3_scraper.auth.Token | None=None, gtoken: splatnet3_scraper.auth.Token | None=None, bullet_token: splatnet3_scraper.auth.Token | None=None):
    """Given any of the three tokens used for Splatnet authentication, updates a user's tokens based on the given Discord UID."""
    WHERE = f"WHERE uid = '{uid}'"
    if not db:
        load_dotenv()
        db = mysql.connector.connect(
        host=os.getenv('SERVER_NAME'),
        user=os.getenv('USER_NAME'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DB_NAME')
        )
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM tokens WHERE uid = {uid}")
    result = cursor.fetchall()
    if len(result):
        if session_token:
            cursor.execute(f"UPDATE tokens SET st_val = '{session_token.value}', st_ts = {session_token.timestamp} {WHERE};")
            db.commit()
        if gtoken:
            cursor.execute(f"UPDATE tokens SET gt_val = '{gtoken.value}', gt_ts = {gtoken.timestamp} {WHERE};")
            db.commit()
        if bullet_token:
            cursor.execute(f"UPDATE tokens SET bt_val = '{bullet_token.value}', bt_ts = {bullet_token.timestamp} {WHERE};")
            db.commit()
    else:
        cursor.execute(f"INSERT INTO tokens (uid, st_val, st_ts) VALUES ('{uid}','{session_token.value}',{session_token.timestamp});")
        db.commit()
        print(f"Registered user {uid}")
    cursor.close()

def load_tokens(uid: str, opt=0) -> splatnet3_scraper.auth.TokenManager | None:
    """Given a Discord User ID, returns a dict of the 3 tokens belonging to said user in order to construct a TokenManager instance."""
    load_dotenv()
    db = mysql.connector.connect(
    host=os.getenv('SERVER_NAME'),
    user=os.getenv('USER_NAME'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('DB_NAME')
    )
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM tokens WHERE uid = {uid}")
    result = cursor.fetchall()
    if result:
        token_man = splatnet3_scraper.auth.TokenManagerConstructor.from_session_token(result[0][1])
        token_man.nso._version = constants.VERSION_OVERRIDE
        if result[0][3]:
            token_man.add_token(result[0][3], name="gtoken", timestamp=float(result[0][4]))
        elif opt==0:
            token_man.generate_gtoken()
            insert_tokens(uid, db, gtoken=token_man.get_token("gtoken"))
        if result[0][5]:
            token_man.add_token(result[0][5], name="bullet_token", timestamp=float(result[0][6]))
        elif opt==0:
            token_man.generate_bullet_token()  
            insert_tokens(uid, db, bullet_token=token_man.get_token("bullet_token"))
        if opt==0:
            if prefetch_checks(token_man.get_token("gtoken"), token_man.get_token("bullet_token")):
                token_man.generate_gtoken()
                token_man.generate_bullet_token()
                insert_tokens(uid, db, gtoken=token_man.get_token("gtoken"), bullet_token=token_man.get_token("bullet_token"))
        db.close()
        return token_man
    else:
        return None

def prefetch_checks(g: splatnet3_scraper.auth.Token, b: splatnet3_scraper.auth.Token) -> bool:
        """Executes a simple query to the Splatnet API in order to verify that the g and bullet tokens are valid. Returns FALSE if the query is successful, returns TRUE if the query fails."""
        gql = splatnet3_scraper.auth.GraphQLQueries()
        graphql_body = {"extensions": {"persistedQuery": {"sha256Hash": constants.sha_keys["HomeQuery"],"version": 1}},"variables":{"naCountry":"US"}}
        test = requests.post(constants.SPLATNET_URL + "/api/graphql", data=json.dumps(graphql_body), headers=gql.query_header(bullet_token=b.value, language="en-US"), cookies=dict(_gtoken=g.value))
        return test.status_code!=200

def get_replay(token_man: splatnet3_scraper.auth.TokenManager, code: str):
    """Executes a query and returns a dict consisting of replay data using the Tokens in the given TokenManager instance and the specified Replay Code."""
    if len(code)!=16:
        code=replay_code(code)
        if code=="INVALID":
            return "invalid replay code format"
    g = token_man.get_token("gtoken")
    b = token_man.get_token("bullet_token")
    gql = splatnet3_scraper.auth.GraphQLQueries()
    graphql_body = {"extensions": {"persistedQuery": {"sha256Hash": constants.sha_keys["DownloadSearchReplayQuery"],"version": 1}},"variables": { "code": code }}
    query = requests.post(constants.SPLATNET_URL + "/api/graphql", data=json.dumps(graphql_body), headers=gql.query_header(bullet_token=b.value, language="en-US"), cookies=dict(_gtoken=g.value))
    if query.status_code == 200:
        response = json.loads(query.text)
        return response["data"]
    else:
        print(f'Error: {query.status_code}')
        print(query.headers)

def get_replay_history(token_man: splatnet3_scraper.auth.TokenManager):
    """Executes multiple queries and returns a dict consisting of data from multiple replays using the Tokens in the given TokenManager instance and the specified Replay Code."""
    g = token_man.get_token("gtoken")
    b = token_man.get_token("bullet_token")
    gql = splatnet3_scraper.auth.GraphQLQueries()
    graphql_body = {"extensions": {"persistedQuery": {"sha256Hash": constants.sha_keys["ReplayQuery"],"version": 1}},"variables":{"naCountry":"US"}}
    query = requests.post(constants.SPLATNET_URL + "/api/graphql", data=json.dumps(graphql_body), headers=gql.query_header(bullet_token=b.value, language="en-US"), cookies=dict(_gtoken=g.value))
    if query.status_code == 200:
        response = json.loads(query.text)
        return response['data']['replays']['nodes']
    else:
        print(f'Error: {query.status_code}')
        print(query.headers)

def queue_download(token_man: splatnet3_scraper.auth.TokenManager, replay_id: str):
    """Executes a query that queues a replay to be downloaded from the lobby terminal in-game from a given replay ID (only accessible by scraping replay data). Uses the tokens in the given TokenManager instance."""
    g = token_man.get_token("gtoken")
    b = token_man.get_token("bullet_token")
    gql = splatnet3_scraper.auth.GraphQLQueries()
    graphql_body = {"extensions": {"persistedQuery": {"sha256Hash": constants.sha_keys["ReplayModalReserveReplayDownloadMutation"],"version": 1}},"variables": { "input": { "id": replay_id } }}
    query = requests.post(constants.SPLATNET_URL + "/api/graphql", data=json.dumps(graphql_body), headers=gql.query_header(bullet_token=b.value, language="en-US"), cookies=dict(_gtoken=g.value))
    if query.status_code == 200:
        response = json.loads(query.text)
        return response["data"]["reserveReplayDownload"]
    else:
        return query
    
def queue_batch_download(token_man: splatnet3_scraper.auth.TokenManager, replay_ids: list[str]):
    """Executes multiple queries that queue all replays passed through via their IDs to be downloaded from the lobby terminal in-game."""
    g = token_man.get_token("gtoken")
    b = token_man.get_token("bullet_token")
    gql = splatnet3_scraper.auth.GraphQLQueries()
    success=0
    for id in replay_ids:
        graphql_body = {"extensions": {"persistedQuery": {"sha256Hash": constants.sha_keys["ReplayModalReserveReplayDownloadMutation"],"version": 1}},"variables": { "input": { "id": id } }}
        query = requests.post(constants.SPLATNET_URL + "/api/graphql", data=json.dumps(graphql_body), headers=gql.query_header(bullet_token=b.value, language="en-US"), cookies=dict(_gtoken=g.value))
        if query.status_code==200:
            success+=1
    return success

def get_album(token_man: splatnet3_scraper.auth.TokenManager):
    """Executes a query to get and display the photos recently shared to Splatnet. A number of photos to grab can be specified. If there is no number, all available photos are grabbed."""
    g = token_man.get_token("gtoken")
    b = token_man.get_token("bullet_token")
    gql = splatnet3_scraper.auth.GraphQLQueries()
    graphql_body = {"extensions": {"persistedQuery": {"sha256Hash": constants.sha_keys["PhotoAlbumQuery"],"version": 1}},"variables":{"naCountry":"US"}}
    query = requests.post(constants.SPLATNET_URL + "/api/graphql", data=json.dumps(graphql_body), headers=gql.query_header(bullet_token=b.value, language="en-US"), cookies=dict(_gtoken=g.value))
    if query.status_code == 200:
        response = json.loads(query.text)
        try:
            return response['data']['photoAlbum']['items']['nodes']
        except:
            return None
    else:
        return None
    


def get_user_info(token_man: splatnet3_scraper.auth.TokenManager):
    """Executes a simple query to grab the name and user icon of the user initiating the command. This is to make replay embeds look even prettier."""
    g = token_man.get_token("gtoken")
    b = token_man.get_token("bullet_token")
    gql = splatnet3_scraper.auth.GraphQLQueries()
    graphql_body = {"extensions": {"persistedQuery": {"sha256Hash": constants.sha_keys["SettingQuery"],"version": 1}},"variables":{"naCountry":"US"}}
    query = requests.post(constants.SPLATNET_URL + "/api/graphql", data=json.dumps(graphql_body), headers=gql.query_header(bullet_token=b.value, language="en-US"), cookies=dict(_gtoken=g.value))
    response = json.loads(query.text)
    return (response["data"]["currentPlayer"]["name"], response["data"]["currentPlayer"]["userIcon"]["url"])

def replay_code(code: str) -> str:
    """Formats a given replay code between two formats; XXXX-XXXX-XXXX-XXXX and XXXXXXXXXXXXXXXX, while also correcting commonly typo'd characters. If the replay code is the incorrect length, returns 'INVALID'."""
    code = code.upper()
    trnsl = str.maketrans("IOZ","102") # replay codes CANNOT contain I, O, or Z since they can be easily mistaken for 1, 0, and 2. however, people still mistakingly type them in lol.
    code = code.translate(trnsl)
    if len(code)==19:
        code = code.split('-')
        short = ""
        for portion in code:
            short += portion
        return short
    elif len(code)==16:
        return code[:4] + '-' + code[4:8] + '-' + code[8:12] + '-' + code[12:]
    else:
        return "INVALID"
    
def create_batch_bin(ids: list[str]):
    """Creates a replay batch file to allow queue_batch_download() to have a list of replay IDs to use."""
    batch=bytearray()
    for replayID in ids:
        if replayID != '--------':
            batch.extend(replayID.encode(encoding="ascii"))
            batch.extend(">".encode(encoding="ascii"))
    return batch

def read_batch_bin(batch: bytes):
    """Helper function for queue_batch_download() that parses a binary replay batch file and returns a list of replay IDs to queue."""
    batch = batch.decode(encoding="ascii")
    batch = batch.split(">")
    batch.pop()
    return batch

if __name__ == "__main__":
    code = input("replay code:")
    print(replay_code(code))
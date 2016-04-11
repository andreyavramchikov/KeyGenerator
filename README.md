This application use sqlite database;

To run the application you should first apply migrations

In migration: 0002 I generated 1000 unique keys which will be all keys which system can provide
by default all keys are 'NOT ISSUED'

All the urls should end with trailing slash.

GET REQUESTS:
    http://yourhost/api/info/ - Return amount of not ISSUED keys
    http://yourhost/api/status?key=yourkey - Return status of key - (ISSUED, NOT ISSUED, REPAID)
    http://yourhost/api/getkey/

POST REQUESTS:
    http://yourhost/api/repay/ You should specify payload: {key: 'keytorepay'}

Examples:
   http://127.0.0.1:9001/api/getkey/
   http://127.0.0.1:9001/api/status?key=12dF
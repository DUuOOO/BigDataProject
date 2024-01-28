import orjson
from elasticsearch8 import helpers
from elasticsearch8.helpers import streaming_bulk

es_cli = Elasticsearch(hosts="", basic_auth=('',''),
                            verify_certs = False,
                            retry_on_timeout=True)

def data_generator(file):
    print(f"reading {file}")
    with open(file,'r', encoding='utf-8') as f:
        for line in f:
            dic = orjson.loads(line)
            yield dic

def topic_action(file):  # 响应入库
    chunk_size = 100
    errors_before_interrupt = 5
    refresh_index_after_insert = False
    max_insert_retries = 3
    yield_ok = False
    for ok, result in streaming_bulk(es_cli, data_generator(file), chunk_size=chunk_size, request_timeout=60 * 3, yield_ok=yield_ok):
        if ok is not True:
            errors_count += 1
    print(file + ' update successfully!')

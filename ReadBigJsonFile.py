# when read a format json file like [{},{},{}], through tries
# read by line is a best methods, but remember to read in chunks
# this could avoid concatenating a big list and affect the effiency
# what is more, remember to handle the remaind data
def read_file_info(file):
    data = []
    count = 0
    with open(file) as fp:
        for line in fp:
            count += 1
            dic = orjson.loads(line)
            data.append(dic)
            if count == 100000:
                topic_action(data)
                data = []
                count = 0
    Handlefunction(data)
    print('read end')
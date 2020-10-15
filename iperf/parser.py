import re


def parse_result(result):
    out, err = result
    stats = dict()
    stats['ip'] = re.findall(r'local \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
                             out)[0].split(' ')[1]
    stats['interval'] = ' '.join(re.split(' +', re.findall(r'\d\.\d{2}-\d{1,2}\.\d{2}.*sender',
                                                           out)[0])[:2])
    stats['transfer'] = ' '.join(re.findall(r'\d\.\d{2} [GM]Bytes.*sender',
                                            out)[0].split(' ')[:2])
    stats['bandwidth'] = ' '.join(re.findall(r'\d{2,4} [GM]bits.*sender',
                                             out)[0].split(' ')[:2])
    if err:
        return {
            "status": 255,
            "error": err,
            "result": stats
        }
    return {
        "status": 0,
        "error": None,
        "result": stats
    }

import re

IP_REGEX = r'local \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
INTERVAL_REGEX = r'\d\.\d{2}-\d{1,2}\.\d{2}.*sender'
TRANSFER_REGEX = r'\d\.\d{2} [GM]Bytes.*sender'
BANDWIDTH_REGEX = r'\d{2,4} [GM]bits.*sender'


def parse_result(result):
    out, err = result
    stats = dict()
    stats['ip'] = re.findall(IP_REGEX, out)[0].split(' ')[1]
    stats['interval'] = ' '.join(re.split(' +', re.findall(INTERVAL_REGEX,
                                                           out)[0])[:2])
    stats['transfer'] = ' '.join(re.findall(TRANSFER_REGEX,
                                            out)[0].split(' ')[:2])
    stats['bandwidth'] = ' '.join(re.findall(BANDWIDTH_REGEX,
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

"""docstring for ElasticsearchLogHandler"""
import logging
import requests
import json
import datetime
from urllib.parse import urljoin


class ElasticsearchLogHandler(logging.Handler):
    """docstring for ElasticsearchLogHandler"""

    def __init__(self, es_host, es_log_index_name="lad", es_log_type="commonlog"):
        super(ElasticsearchLogHandler, self).__init__()
        self.es_host = es_host
        self.es_log_index_name = es_log_index_name + "-"
        self.es_log_type = es_log_type

        print(
            "Elasticsearch logging enabled to es_host: {0}, index: {1}, type: {2}".format(
                self.es_host, self.es_log_index_name, self.es_log_type
            )
        )

    def emit(self, record):
        log_entry = self.format(record)
        url = (
            urljoin(
                str(self.es_host),
                str(
                    self.es_log_index_name
                    + datetime.datetime.now().strftime("%Y.%m.%d")
                ),
            )
            + "/"
            + str(self.es_log_type)
        )
        data = {"message": log_entry, "@timestamp": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")}
        content = requests.post(
            url, data=json.dumps(data), headers={"Content-Type": "application/json"}
        ).content

        return content

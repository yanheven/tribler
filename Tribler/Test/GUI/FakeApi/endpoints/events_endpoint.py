import json
from twisted.web import server, resource
from Tribler.Core.version import version_id


class EventsEndpoint(resource.Resource):

    isLeaf = True

    def __init__(self):
        resource.Resource.__init__(self)
        self.event_request = None

    def on_search_results_channels(self, results):
        for result in results:
            self.event_request.write(json.dumps({"type": "search_result_channel", "event": {"result": result}}) + '\n')

    def on_search_results_torrents(self, results):
        for result in results:
            self.event_request.write(json.dumps({"type": "search_result_torrent", "event": {"result": result}}) + '\n')

    def render_GET(self, request):
        self.event_request = request

        request.write(json.dumps({"type": "events_start", "event": {"tribler_started": True,
                                                                    "version": version_id}}) + '\n')
        request.write(json.dumps({"type": "tribler_started"}) + '\n')

        return server.NOT_DONE_YET
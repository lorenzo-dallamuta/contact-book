from rest_framework.routers import DefaultRouter


class CustomDefaultRouter(DefaultRouter):
    """
    this router is going to accept queries that possess as well as queries
    that don't possess a trailing slash between the url and the query param
     """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trailing_slash = '/?'

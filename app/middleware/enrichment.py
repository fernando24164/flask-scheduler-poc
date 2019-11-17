from db import redis


class Enrichment():
    """Middleware to enrich data endpoint
    
    Returns:
        [type] -- [description]
    """    

    def __call__(self):
        return True
from dataclasses import dataclass, asdict

@dataclass()
class CampaignMeta:
    account_id: str
    name: str
    objective: str
    #campaign_type: str
    #placement: list
    #ad_type: str
    #locale: str
    #device_platform: str
    #details: dict
    status: str = 'paused'
    #source_campaign_id: str = None
    campaign_id: str = None

    def to_dict(self):
        return asdict(self)
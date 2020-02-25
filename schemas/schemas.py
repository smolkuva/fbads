from marshmallow import Schema, fields, post_load
from marshmallow.validate import OneOf

from facebook_business.adobjects.campaign import Campaign as FBCampaign

from metas.campaign import CampaignMeta

class CampaignSchema(Schema):
    account_id = fields.Str(required=True)
    name = fields.Str(required=True)
    objective = fields.Str(required=True)
    #campaign_type = fields.Str(required=True)
    #placement = fields.List(fields.String(required=True), required=True)
    #ad_type = fields.Str(required=True)
    #locale = fields.Str(required=True)
    #device_platform = fields.Str(required=True)
    #details = fields.Dict(values=fields.String(), keys=fields.String(), required=False)
    status = fields.Str(missing=None, validate=OneOf([
        FBCampaign.Status.active,
        FBCampaign.Status.paused,
        FBCampaign.Status.deleted,
        FBCampaign.Status.archived
    ]))

    @post_load
    def convert_to_object(self, data):
        campaign = CampaignMeta(**data)
        return campaign
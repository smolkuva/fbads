from campaign import CampaignCreator
from schemas.schemas import CampaignSchema

from facebook_business.api import FacebookAdsApi

from facebook_business.adobjects.adaccount import AdAccount as FbAdAccount

FacebookAdsApi.init(access_token='')

REQUEST = dict(account_id='', name='test_campaign_for_fb_ads_management_approval_test', objective='LINK_CLICKS')

# schema = CampaignSchema()
#
# campaign_meta, errors = schema.load(REQUEST)
#
# campaigncreator = CampaignCreator(campaign_meta)
# campaign_id = campaigncreator.create()
# print(campaign_id)
#
#
fields = [
  'name',
  'objective',
]
params = {
  'effective_status': ['ACTIVE','PAUSED'],
}
print(FbAdAccount('act_').get_campaigns(fields=fields, params=params))
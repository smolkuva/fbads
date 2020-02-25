from abc import ABC
import logging
import time

from facebook_business.adobjects.campaign import Campaign as FbCampaign
from facebook_business.adobjects.adaccount import AdAccount as FbAdAccount
from facebook_business.exceptions import FacebookRequestError

from metas.campaign import CampaignMeta
from utils.field_spec import campaign_fields as campaign_create_fields


logging.basicConfig(level=logging.INFO)


class CampaignCreator(ABC):

    def __init__(self, campaign: CampaignMeta):
        self.campaign = campaign
        self.account = FbAdAccount('act_' + campaign.account_id)

    def create(self):
        if self.campaign.campaign_id:
            return self.campaign.campaign_id

        campaign_create_params = {
            FbCampaign.Field.name: self.campaign.name,
            FbCampaign.Field.objective: self.campaign.objective,
            FbCampaign.Field.status: self.campaign.status
        }

        fb_campaign: FbCampaign = self._fb_create(campaign_create_params, campaign_create_fields)

    def _fb_create(self, params: dict, fields: dict) -> FbCampaign:
        while True:
            try:
                fb_campaign: FbCampaign = self.account.create_campaign(params=params, fields=fields)
            except FacebookRequestError as e:
                if e.http_status() == 80004:
                    logging.info("Too may calls have been made to this account, wait for 15 seconds")
                    time.sleep(15)
                elif e.http_status() == 100 or e.http_status() == 200 or e.http_status() == 294:
                    logging.info("generic error, waiting for 5 seconds")
                    time.sleep(5)
                else:
                    logging.info(e)
                    logging.info(e.http_status())
                    logging.info(e.api_error_code())
                    logging.error("Error in campaign creation")
                    raise e
            break

        return fb_campaign


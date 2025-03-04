# Copyright (c) 2024  Fortinet Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""

"""

from fadc_octavia_provider.fortiadc_agent.fadc_api.slb.real_server_pool import RSpool
from oslo_log import log as logging

LOG = logging.getLogger(__name__)

class Pool(object):

    def __init__(self, fadc_driver):
        self.rspool = RSpool(fadc_driver.host, fadc_driver.connector, fadc_driver.conf.debug_mode)

    def create(self, pool):
        LOG.debug("create pool")
        self.rspool.create(pool)

    def delete(self, pool):
        LOG.debug("delete pool")
        self.rspool.delete(pool)

    def update(self, pool):
        LOG.debug("update pool")
        self.rspool.update(pool)



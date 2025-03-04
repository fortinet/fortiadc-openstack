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

from octavia.api.drivers import utils as provider_utils
from fadc_octavia_provider.fortiadc_agent.flows import health_monitor_flows
from fadc_octavia_provider.fortiadc_agent.flows import listener_flows
from fadc_octavia_provider.fortiadc_agent.flows import load_balancer_flows
from fadc_octavia_provider.fortiadc_agent.flows import member_flows
from fadc_octavia_provider.fortiadc_agent.flows import pool_flows


LB_FLOWS = load_balancer_flows.LoadBalancerFlows()
HM_FLOWS = health_monitor_flows.HealthMonitorFlows()
LISTENER_FLOWS = listener_flows.ListenerFlows()
M_FLOWS = member_flows.MemberFlows()
P_FLOWS = pool_flows.PoolFlows()


def get_create_load_balancer_flow(topology, listeners=None):
    return LB_FLOWS.get_create_load_balancer_flow(topology,
                                                  listeners=listeners)


def get_delete_load_balancer_flow(lb):
    return LB_FLOWS.get_delete_load_balancer_flow(lb)


def get_listeners_on_lb(db_lb):
    """Get a list of the listeners on a load balancer.

    :param db_lb: A load balancer database model object.
    :returns: A list of provider dict format listeners.
    """
    listener_dicts = []
    for listener in db_lb.listeners:
        prov_listener = provider_utils.db_listener_to_provider_listener(
            listener)
        listener_dicts.append(prov_listener.to_dict())
    return listener_dicts


def get_pools_on_lb(db_lb):
    """Get a list of the pools on a load balancer.

    :param db_lb: A load balancer database model object.
    :returns: A list of provider dict format pools.
    """
    pool_dicts = []
    for pool in db_lb.pools:
        prov_pool = provider_utils.db_pool_to_provider_pool(pool)
        pool_dicts.append(prov_pool.to_dict())
    return pool_dicts


def get_cascade_delete_load_balancer_flow(lb, listeners=(), pools=()):
    return LB_FLOWS.get_cascade_delete_load_balancer_flow(lb, listeners,
                                                          pools)


def get_update_load_balancer_flow():
    return LB_FLOWS.get_update_load_balancer_flow()

def get_create_health_monitor_flow():
    return HM_FLOWS.get_create_health_monitor_flow()


def get_delete_health_monitor_flow():
    return HM_FLOWS.get_delete_health_monitor_flow()


def get_update_health_monitor_flow():
    return HM_FLOWS.get_update_health_monitor_flow()


def get_create_listener_flow():
    return LISTENER_FLOWS.get_create_listener_flow()


def get_create_all_listeners_flow():
    return LISTENER_FLOWS.get_create_all_listeners_flow()


def get_delete_listener_flow():
    return LISTENER_FLOWS.get_delete_listener_flow()


def get_update_listener_flow():
    return LISTENER_FLOWS.get_update_listener_flow()


def get_create_member_flow():
    return M_FLOWS.get_create_member_flow()


def get_delete_member_flow():
    return M_FLOWS.get_delete_member_flow()


def get_update_member_flow():
    return M_FLOWS.get_update_member_flow()


def get_batch_update_members_flow(old_members, new_members, updated_members):
    return M_FLOWS.get_batch_update_members_flow(old_members, new_members,
                                                 updated_members)

def get_create_pool_flow():
    return P_FLOWS.get_create_pool_flow()


def get_delete_pool_flow():
    return P_FLOWS.get_delete_pool_flow()


def get_update_pool_flow():
    return P_FLOWS.get_update_pool_flow()

def get_delete_pools_member_health_flow(pools):
    return P_FLOWS.get_delete_pools_member_health_flow(pools)

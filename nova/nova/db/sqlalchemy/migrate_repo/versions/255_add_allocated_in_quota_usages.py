# Copyright 2013 Intel Corporation
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

from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Integer


def upgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    # Add a new column metrics to save metrics info for compute nodes
    quota_usages = Table('quota_usages', meta, autoload=True)
    shadow_quota_usages = Table('shadow_quota_usages', meta, autoload=True)

    allocated = Column('allocated', Integer, nullable=False)
    shadow_allocated= Column('allocated', Integer, nullable=False)
    quota_usages.create_column(allocated)
    shadow_quota_usages.create_column(shadow_allocated)


def downgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    # Remove the new column
    quota_usages = Table('quota_usages', meta, autoload=True)
    shadow_quota_usages = Table('shadow_quota_usages', meta, autoload=True)

    quota_usages.drop_column('allocated')
    shadow_quota_usages.drop_column('allocated')

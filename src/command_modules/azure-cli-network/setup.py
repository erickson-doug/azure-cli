#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from codecs import open
from setuptools import setup

VERSION = '0.1.2rc1+dev'

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = [
    'azure-mgmt-network==0.30.0',
    'azure-mgmt-trafficmanager==0.30.0rc6',
    'azure-mgmt-dns==1.0.0',
    'azure-mgmt-resource==0.30.2',
    'azure-cli-core'
]

with open('README.rst', 'r', encoding='utf-8') as f:
    README = f.read()
with open('HISTORY.rst', 'r', encoding='utf-8') as f:
    HISTORY = f.read()

setup(
    name='azure-cli-network',
    version=VERSION,
    description='Microsoft Azure Command-Line Tools Network Command Module',
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    author='Microsoft Corporation',
    author_email='azpycli@microsoft.com',
    url='https://github.com/Azure/azure-cli',
    classifiers=CLASSIFIERS,
    namespace_packages=[
        'azure',
        'azure.cli',
        'azure.cli.command_modules',
    ],
    packages=[
        'azure.cli.command_modules.network',
        'azure.cli.command_modules.network.mgmt_app_gateway',
        'azure.cli.command_modules.network.mgmt_app_gateway.lib',
        'azure.cli.command_modules.network.mgmt_app_gateway.lib.models',
        'azure.cli.command_modules.network.mgmt_app_gateway.lib.operations',
        'azure.cli.command_modules.network.mgmt_vnet',
        'azure.cli.command_modules.network.mgmt_vnet.lib',
        'azure.cli.command_modules.network.mgmt_vnet.lib.models',
        'azure.cli.command_modules.network.mgmt_vnet.lib.operations',
        'azure.cli.command_modules.network.mgmt_public_ip',
        'azure.cli.command_modules.network.mgmt_public_ip.lib',
        'azure.cli.command_modules.network.mgmt_public_ip.lib.models',
        'azure.cli.command_modules.network.mgmt_public_ip.lib.operations',
        'azure.cli.command_modules.network.mgmt_lb',
        'azure.cli.command_modules.network.mgmt_lb.lib',
        'azure.cli.command_modules.network.mgmt_lb.lib.models',
        'azure.cli.command_modules.network.mgmt_lb.lib.operations',
        'azure.cli.command_modules.network.mgmt_nsg',
        'azure.cli.command_modules.network.mgmt_nsg.lib',
        'azure.cli.command_modules.network.mgmt_nsg.lib.models',
        'azure.cli.command_modules.network.mgmt_nsg.lib.operations',
        'azure.cli.command_modules.network.mgmt_nic',
        'azure.cli.command_modules.network.mgmt_nic.lib',
        'azure.cli.command_modules.network.mgmt_nic.lib.models',
        'azure.cli.command_modules.network.mgmt_nic.lib.operations',
        'azure.cli.command_modules.network.mgmt_local_gateway',
        'azure.cli.command_modules.network.mgmt_local_gateway.lib',
        'azure.cli.command_modules.network.mgmt_local_gateway.lib.models',
        'azure.cli.command_modules.network.mgmt_local_gateway.lib.operations',
        'azure.cli.command_modules.network.mgmt_vnet_gateway',
        'azure.cli.command_modules.network.mgmt_vnet_gateway.lib',
        'azure.cli.command_modules.network.mgmt_vnet_gateway.lib.models',
        'azure.cli.command_modules.network.mgmt_vnet_gateway.lib.operations',
        'azure.cli.command_modules.network.mgmt_vnet_gateway',
        'azure.cli.command_modules.network.mgmt_vnet_gateway.lib',
        'azure.cli.command_modules.network.mgmt_vnet_gateway.lib.models',
        'azure.cli.command_modules.network.mgmt_vnet_gateway.lib.operations',
        'azure.cli.command_modules.network.mgmt_express_route_circuit',
        'azure.cli.command_modules.network.mgmt_express_route_circuit.lib',
        'azure.cli.command_modules.network.mgmt_express_route_circuit.lib.models',
        'azure.cli.command_modules.network.mgmt_express_route_circuit.lib.operations',
        'azure.cli.command_modules.network.mgmt_traffic_manager_profile',
        'azure.cli.command_modules.network.mgmt_traffic_manager_profile.lib',
        'azure.cli.command_modules.network.mgmt_traffic_manager_profile.lib.models',
        'azure.cli.command_modules.network.mgmt_traffic_manager_profile.lib.operations',
        'azure.cli.command_modules.network.zone_file'
    ],
    install_requires=DEPENDENCIES,
)

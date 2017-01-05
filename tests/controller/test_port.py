#!/usr/bin/env python
#
# Copyright (C) 2016 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gns3server.controller.ports.ethernet_port import EthernetPort


def test_short_name():
    # If no customization of port name format return the default short name
    assert EthernetPort("Ethernet0", 0, 0, 0).short_name == "e0/0"
    # If port name format has change we use the port name as the short name (1.X behavior)
    assert EthernetPort("eth0", 0, 0, 0).short_name == "eth0"

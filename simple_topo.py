# Copyright 2014 Eliseu Silva Torres
#
# This file is part of MininetWeb.
#
# MininetWeb is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MininetWeb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MininetWeb.  If not, see <http://www.gnu.org/licenses/>.


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
 
class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def __init__(self, n=2, **opts):
        Topo.__init__(self, **opts)
        switch = self.addSwitch('s1')
        for h in range(n):
            """Add hosts"""
            host = self.addHost('h%s' % (h + 1))
            """add links"""
            self.addLink(host, switch)

def perfTest(hosts=2):
    "Create network and run simple performance test"
    n = hosts
    topo = SingleSwitchTopo(n)
    net = Mininet(topo=topo)
    return net
     
if __name__=='__main__':
    setLogLevel('info')
    perfTest()
            

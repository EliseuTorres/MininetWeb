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



from flask import Flask, request, redirect, url_for, abort, render_template, flash

from simple_topo import perfTest
from mininet.util import dumpNodeConnections


app = Flask(__name__)
app.config.from_object(__name__)



app.debug = True

@app.route('/')
def index():    
    return render_template('menu.html')

@app.route('/start_topo', methods=['POST'])
def start_topo():
    global hosts
    hosts = request.form['host']
    hosts = int(hosts)
    return redirect(url_for('simple_topo'))

@app.route('/simple_topo')
def simple_topo():
    global hosts
    global net
    net = perfTest(hosts=hosts)
    net.start()
    return render_template('simple_topo.html', hosts=hosts)


@app.route('/option', methods=['POST'])
def option():
    option = request.form['option']
    global h1
    global h2
    global hosts
    if option == "ping":        
        if not request.form['host1'] or not request.form['host2']:
            result = "Hosts precisam ser selecionados"
            return render_template('simple_topo.html', hosts=hosts, result=result)
        else:
            h1 = request.form['host1']        
            h2 = request.form['host2']
            return redirect(url_for('ping'))
    elif option == "iperf":
        if not request.form['host1'] or not request.form['host2']:
            result = "Hosts precisam ser selecionados"
            return render_template('simple_topo.html', hosts=hosts, result=result)
        else:
            h1 = request.form['host1']        
            h2 = request.form['host2']        
            return redirect(url_for('iperf'))
    elif option == "iperf2":
        if not request.form['host1'] or not request.form['host2']:
            result = "Hosts precisam ser selecionados"
            return render_template('simple_topo.html', hosts=hosts, result=result)
        else:
            h1 = request.form['host1']        
            h2 = request.form['host2']        
            return redirect(url_for('iperf2'))
    elif option == "up":
        if not request.form['host1']:
            result = "Selecione o Host"
            return render_template('simple_topo.html', hosts=hosts, result=result)
        else:
            h1 = request.form['host1']                    
            return redirect(url_for('up'))
    elif option == "down":        
        if not request.form['host1']:
            result = "Selecione o Host"
            return render_template('simple_topo.html', hosts=hosts, result=result)
        else:
            h1 = request.form['host1']                    
            return redirect(url_for('down'))
    
    elif option == "stop":
        global net
        net.stop()
        return render_template('menu.html')

@app.route('/ping')
def ping():
    global net
    global h1
    global h2
    global hosts
    host1, host2 = net.get(h1, h2)
    result = host1.cmd('ping -c 3 ' + host2.IP())    
    return render_template('simple_topo.html', hosts=hosts, result=result)

@app.route('/iperf')
def iperf():
    global net
    global h1
    global h2
    global hosts
    host1, host2 = net.get(h1, h2)
    result = net.iperf((host1, host2))    
    return render_template('simple_topo.html', hosts=hosts, result=result)

@app.route('/iperf2')
def iperf2():
    global net
    global h1
    global h2
    global hosts    
    host1, host2 = net.get(h1, h2)
    host2.cmd('iperf -s &')    
    result = host1.cmd('iperf -c ' + host2.IP())    
    return render_template('simple_topo.html', hosts=hosts, result=result)

@app.route('/up')
def up():
    global net
    global h1    
    global hosts
    host = str(h1)
    net.configLinkStatus( 's1', host, 'up' )
    return render_template('simple_topo.html', hosts=hosts)

@app.route('/down')
def down():
    global net
    global h1    
    global hosts
    host = str(h1)    
    net.configLinkStatus( 's1', host , 'down' )    
    return render_template('simple_topo.html', hosts=hosts)





if __name__== '__main__':
    app.run(host='0.0.0.0')

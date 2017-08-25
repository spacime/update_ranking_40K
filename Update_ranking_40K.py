from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
import configuration as config
# from Ssh_server_ops import Ssh_server_ops
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), './libs', 'ssh_operations'))
import server_operate as server_ops


class MyBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = "This "
        arguments = [
            ( ['-f', '--foo'],
              dict(action='store', help='the notorious foo option') ),
            ( ['-C'],
              dict(action='store_true', help='the big C option') ),
            ]

    @expose(hide=True)
    def default(self):
        # self.app.log.info('Inside MyBaseController.default()')
        print "What operation do you want?"
        print "1) Restart the server"
        print "2) Update the server to newest version"
        print config.configuration['name_server']
        # sshops = Ssh_server_ops()
        server_ops.run()
        if self.app.pargs.foo:
            print("Recieved option: foo => %s" % self.app.pargs.foo)

    @expose(help="this command does relatively nothing useful")
    def command1(self):
        self.app.log.info("Inside MyBaseController.command1()")

    @expose(aliases=['cmd2'], help="more of nothing")
    def command2(self):
        self.app.log.info("Inside MyBaseController.command2()")


class MySecondController(CementBaseController):
    class Meta:
        label = 'second'
        stacked_on = 'base'

    @expose(help='this is some command', aliases=['some-cmd'])
    def second_cmd1(self):
        self.app.log.info("Inside MySecondController.second_cmd1")


class MyApp(CementApp):
    class Meta:
        label = 'myapp'
        base_controller = 'base'
        handlers = [MyBaseController, MySecondController]



with MyApp() as app:
    app.run()
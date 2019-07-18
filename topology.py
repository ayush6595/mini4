from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        FirstHost = self.addHost( 'h1' )
        SecondHost = self.addHost( 'h2' )
        ThirdHost = self.addHost( 'h3' )
       
        firstSwitch = self.addSwitch( 's1' )
       

        # Add links
        self.addLink( firstSwitch, FirstHost )
       self.addLink( firstSwitch, secondHost )
       self.addLink( firstSwitch, thirdHost )
       
    #   self.addLink( secondSwitch, SecondHost )
    #   self.addLink( thirdSwitch, ThirdHost )
    #   self.addLink( fourthSwitch, FourthHost )
    #   self.addLink( fifthSwitch, FifthHost )
    #   self.addLink( sixthSwitch, SixthHost )
    #    self.addLink( firstSwitch, secondSwitch  )
    #    self.addLink( secondSwitch, thirdSwitch )
    #    self.addLink( thirdSwitch, sixthSwitch )
    #    self.addLink( fourthSwitch, sixthSwitch )
    #    self.addLink( fourthSwitch, thirdSwitch )
    #    self.addLink( firstSwitch, fourthSwitch )
     #   self.addLink( firstSwitch, fifthSwitch )
     #   self.addLink( secondSwitch, fifthSwitch )
     ##  self.addLink( fifthSwitch, thirdSwitch )

topos = { 'mytopo': ( lambda: MyTopo() ) }

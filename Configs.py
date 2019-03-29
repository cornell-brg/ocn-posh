#=========================================================================
# InputUnitRTL.py
#=========================================================================
# This file contains basic configurations for the network generator
# The detailed/internal configurations/parameters can be set in the code
# hierarchy via set_parameter().
#
# Author : Cheng Tan, Yanghui Ou
#   Date : Mar 4, 2019

import argparse

#def configure_network(args):
def configure_network():

  parser = argparse.ArgumentParser()

  parser.add_argument("--topology",         type=str, default="Crossbar",
                    choices=['Crossbar', 'Ring', 'Mesh', 'Torus'],
                    help="topology can be applied in the network.")

  parser.add_argument("--router-latency",   type=int, default=1,
                    action="store",
                    help="number of pipeline stages in router.")

  parser.add_argument("--link-latency",     type=int, default=1, 
                    action="store",
                    help="number of input stages in router.")

  parser.add_argument("--link-width-bits",  type=int, default=128, 
                    action="store",
                    help="width in bits for all links.")

  parser.add_argument("--virtual-channel",  type=int, default=4, 
                    action="store",
                    help="""number of virtual channels.""")

  parser.add_argument("--routing-strategy", type=str, default='DORY',
                    action="store", choices=['DORX', 'DORY', 'WFR', 'NLR'],
                    help="routing algorithm applied in network.")

  parser.add_argument("--routers",          type=int, default=16, 
                    action="store",
                    help="""number of routers in network.""")

  parser.add_argument("--rows",             type=int, default=4, 
                    action="store",
                    help="""number of rows of routers in network.""")

  parser.add_argument("--router-inports",   type=int, default=5, 
                    action="store",
                    help="""number of inports in each router.""")

  parser.add_argument("--router-outports",  type=int, default=5, 
                    action="store",
                    help="""number of outports in each router.""")

#  configs = parser.parse_args(args)
  configs = parser.parse_args( [] )
  return configs


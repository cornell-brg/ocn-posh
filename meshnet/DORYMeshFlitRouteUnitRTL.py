#=========================================================================
# DORYMeshFlitRouteUnitRTL.py
#=========================================================================
# A DOR route unit with get/give interface.
#
# Author : Cheng Tan
#   Date : July 12, 2019

from pymtl3      import *
from directions import *
from pymtl3.stdlib.ifcs import GetIfcRTL, GiveIfcRTL

class DORYMeshFlitRouteUnitRTL( Component ):

  def construct( s, MsgType, PositionType, num_outports = 5 ):

    # Constants 

    s.num_outports = num_outports

    # Interface

    s.get  = GetIfcRTL( MsgType )
    s.give = [ GiveIfcRTL (MsgType) for _ in range ( s.num_outports ) ]
    s.pos  = InPort( PositionType )

    # Componets

    s.out_dir  = Wire( mk_bits( clog2( s.num_outports ) ) )
    s.give_ens = Wire( mk_bits( s.num_outports ) ) 

    # Connections

    for i in range( s.num_outports ):
      s.connect( s.get.msg,     s.give[i].msg )
      s.connect( s.give_ens[i], s.give[i].en  )
    
    # Routing logic
    @s.update
    def up_ru_routing():
 
#      s.out_dir = Bits3(0)
#      s.give[NORTH].rdy = Bits1(0)
#      s.give[SOUTH].rdy = Bits1(0)
#      s.give[WEST ].rdy = Bits1(0)
#      s.give[EAST ].rdy = Bits1(0)
#      s.give[SELF ].rdy = Bits1(0)
      s.give[0].rdy = Bits1(0)
      s.give[1].rdy = Bits1(0)
      s.give[2].rdy = Bits1(0)
      s.give[3].rdy = Bits1(0)
      s.give[4].rdy = Bits1(0)

      if s.get.rdy:
        if s.get.msg.fl_type == 0:
          if s.pos.pos_x == s.get.msg.dst_x and s.pos.pos_y == s.get.msg.dst_y:
  #          s.give[SELF].rdy = Bits1(1)
            s.give[4].rdy = Bits1(1)
            s.out_dir = Bits3( 4 )
          elif s.get.msg.dst_y < s.pos.pos_y:
  #          s.give[SOUTH].rdy = Bits1(1)
            s.give[1].rdy = Bits1(1)
            s.out_dir = Bits3( 1 )
          elif s.get.msg.dst_y > s.pos.pos_y:
  #          s.give[NORTH].rdy = Bits1(1)
            s.give[0].rdy = Bits1(1)
            s.out_dir = Bits3( 0 )
          elif s.get.msg.dst_x < s.pos.pos_x:
  #          s.give[WEST].rdy = Bits1(1)
            s.give[2].rdy = Bits1(1)
            s.out_dir = Bits3( 2 )
          else:
  #          s.give[EAST].rdy = Bits1(1)
            s.give[3].rdy = Bits1(1)
            s.out_dir = Bits3( 3 )
        else:
          s.give[s.out_dir].rdy = Bits1(1)

    @s.update
    def up_ru_get_en():
      s.get.en = s.give_ens > Bits5(0) 

  # Line trace
  def line_trace( s ):

    out_str = [ "" for _ in range( s.num_outports ) ]
    for i in range (s.num_outports):
      out_str[i] = "{}".format( s.give[i] ) 
    return "{}({}){}".format( s.get, "|".join( out_str ) )

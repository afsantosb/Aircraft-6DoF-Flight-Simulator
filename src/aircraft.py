import math
import numpy as np

class State:

  ''' Class used to store and compute the values for the aircraft state
  at a given time instant 't'.

    Each variable will be defined using the following structure:
      <variable name>_<frame of reference(FoR)>_<units>
  
  '''
  
  def __init__(self):
    
    '''
    The state variables are listed in the lines below>

    u_b_mps: longitudinal velocity of the CM wrt inertial FoR resolved in aircraft body fixed/carried FoR
    v_b_mps: lateral velocity of the CM wrt inertial FoR resolved in aircraft body fixed/carried FoR
    w_b_mps: vertical velocity of the CM wrt inertial FoR resolved in aircraft body fixed/carried FoR
    p_b_radps: roll angular velocity of the CM wrt inertial FoR resolved in aircraft body fixed/carried FoR
    q_b_radps: pitch angular velocity of the CM wrt inertial FoR resolved in aircraft body fixed/carried FoR
    r_b_radps: yaw velocity of the CM wrt inertial FoR resolved in aircraft body fixed/carried FoR
    phi_i_rad: roll angle
    theta_i_rad: pitch angle
    psi_i_rad: yaw angle
    x_b_mps: longitudinal position of the aircraft resolved in the inertial FoR
    y_b_mps: lateral position of the aircraft resolved in the inertial FoR
    z_b_mps: vertical position of the aircraft resolved in the inertial FoR
    ail_l_defl_deg: left aileron deflection
    ail_r_defl_deg: right aileron deflection
    elev_l_defl_deg: left elevator deflection
    elev_r_defl_deg: right elevator deflection
    rudder_defl_deg: rudder deflection
    flap_l_defl_deg: left flap deflection
    flap_r_defl_deg: right flap deflection
    hstab_inc_deg: horizontal stabilizer incidence
    
    The state will be initialized with all the variables defined as 0.  
    '''
    
    self.u_b_mps = 0.0
    self.v_b_mps = 0.0
    self.w_b_mps = 0.0
    self.p_b_radps = 0.0
    self.q_b_radps = 0.0
    self.r_b_radps = 0.0
    self.phi_i_rad = 0.0
    self.theta_i_rad = 0.0
    self.psi_i_rad = 0.0
    self.x_b_mps = 0.0 
    self.y_b_mps = 0.0
    self.z_b_mps = 0.0
    self.ail_l_defl_deg = 0.0
    self.ail_r_defl_deg = 0.0
    self.elev_l_defl_deg = 0.0
    self.elev_r_defl_deg = 0.0
    self.rudder_defl_deg = 0.0
    self.flap_l_defl_deg = 0.0
    self.flap_r_defl_deg = 0.0
    self.hstab_inc_deg = 0.0


  def define_state_values_from_JSON(self):
    '''
    TO DO

    Code a method to define aircraft state using a JSON file as an input
    '''

    pass


  def define_state_values(self):
    '''
    TO DO

    Code a method to define aircraft state directly in code
    '''

    pass


  def state_as_array(self):
    '''
    TO DO

    Code a method to define a state vector using numpy array structure
    '''


    pass
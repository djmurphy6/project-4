"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow, math

#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    start = arrow.get(brevet_start_time)     # start time
    num = control_dist_km
    sum = 0.0

    # if checkpoint is further than brevet distance
    if num > brevet_dist_km:
       num = brevet_dist_km         
      # set num to brevet distance, time should be for brevet distance in this case

   # the idea of these if statements is to go by 200km segments, 
   # working from the top down   
    if num > 600 and num <= 1000:
       sum += ((num-600)/28)
       num = 600
    if num > 400 and num <= 600:
       sum += ((num-400)/30)
       num = 400
    if num > 200 and num <= 400:
       sum += ((num-200)/32)
       num = 200
    if num > 0 and num <= 200:
       sum += ((num)/34)
    
    # calculate hours and minutes to shift time by
    hrs = math.floor(sum)
    min = int(round((sum - math.floor(sum))*60, 0))
   
    return start.shift(hours=+hrs, minutes =+ min)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    close = arrow.get(brevet_start_time)

    num = control_dist_km
    sum = 0.0

    # if checkpoint is further than brevet distance
    if num > brevet_dist_km:
       num = brevet_dist_km         
      # set num to brevet distance, time should be for brevet distance in this case
      
    if num < 60:
       sum = (num/20) + 1
    else:
      if num > 600 and num <= 1000:
         sum += ((num-600)/11.428)
         num = 600
      if num > 0 and num <= 600:
         sum += (num/15)
      if num == 0:
         sum = 1
    
    hrs = math.floor(sum)
    min = int(round((sum - math.floor(sum))*60, 0))

    return close.shift(hours =+ hrs, minutes =+ min)

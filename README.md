# snd_rating_model

Working project to create a rating system for player performance in CWL tournaments for Search and Destroy.

Will use data from activision\cwl-data.

Start date 3/20/19


3/24/19: snd ratings v1 is updated with player rating aggregated from the entirety of ww2.
-----------------------------------------------------------------------------------------------------------------------------------------

Current Methodology: The average per round value for kills, non traded kills, firstbloods, time alive, and score streaks earned were derived for each player. The average per round for these stats were calculated for the total aggregation including all players to come up with one mean per stat. This mean (mu) was then subtracted from each players derived per round statistics to average the distribution around the mean (residuals). Since the variation and frequency of occurences per round of some stats resulted in smaller residual stats than others, the data was normalized so each stat has equal weight in the equation. These normalize stats are then summed to obtain the players rating.

The current v1 methodology uploaded removes players who played under 300 rounds of snd during ww2. This can be easily modified with the "threshold_knob" object for different analyses. 
  
Additional analysis and modification will be undergone to create a more informed model for v2.

See: Player_Rating_Calc.ipynb for methodology implementation.

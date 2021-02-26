# Global Terrorism Analysis
<br><br>

Analyzing trends, insights, and understanding the interaction between female education and terrorism.

__Abstract:__
I collected all known global acts of terrorism from the National Consortium for the Study of Terrorism and Responses to Terrorism from the years between 1970 and 2018. This data was analysed to find trends and insight. I have combined this data with global education data to further my analysis. My primary question: does the education of women affect number of terrorist events in a given country?

__Results:__
The education of females is directly correlated to acts of terrorism. This holds for percentage of women without any education and for perentage of women that have completed secondary school. These metrics were used to see if a more stringant standard of education changed the results.

# Background & Motivation
Terrorism is a constant security threat around the world. With more insight into how terrorism works, governments can make better decisions in dealing with present threats. While typical approaches to terrorism involve target hardening and military intervention, I wondered what role education played education. Spesifically, the role of educating females.

My background is in psychotherapy, so I often look to more humanitarian based interventions to global conflict. If we can put a higher evaluation on education and get an outcome of lower terrorism, this would be a desireable approach.

## Terrorism and Education
How a country values and allocates education says a lot about the politics and behaviors of a country. More so in the way a country values the education of women. I combined terrorist dataset found on [http://gtd.terrorismdata.com](https://www.start.umd.edu/data-tools/global-terrorism-database-gtd) with world wide educational statistics found on [https://www.worldbank.org](https://datacatalog.worldbank.org/dataset/global-data-set-education-quality). The two metrics of education I used were percent of women per country that have completed secondary school, and the percent of women per country with no education. I was curious if there was a significant difference between a lower standard of education and a higher one. 

<img src="images/edu_vs_atk.png" width="525"/>

In plotting these two education metrics with acts of terrorism per country, we can see there does seem to be a relationship in the data. On the left it can be seen that the more women which have recieved secondary education is correlated in some way with acts of terror completed. This is the same for women recieving education on the right. As education decreases, terrorism increases.
<img src="images/edu_vs_atk_dis.png" width="525"/>
In order to select an appropriate correlational test, I was interested in the skew of data. It can be seen that both education and acts of terrorism are right skewed and not normally distributed. This informed by decision to use Spearman R correlation.

This test concluded the P-Value was significantly below the alpha threshold of 0.05 with a P-Value of 0.0103 for women which have recieved secondary education and 0.0090 for women that have no education. I can safely reject the H0.

SpearmanrResult(correlation=-0.2277342225532225, pvalue=0.010328712516958242)
Spearman R: SpearmanrResult(correlation=0.23154399207009108, pvalue=0.009088055574197536)


## Limitations
It is important to note correlation does not  equal causation. Terrorism by its very nature is an ourlier event and each organization involved in commiting acts of terror have different ideologies and motivations. Each country is distinct from one another and have their own cultural issues.

## Insights into Terrorism: A Post 9/11 World
In order to trend terrorism, I focused on events after 9/11. The Twin Tower terrorist attack was a moment of global change, in terms of politics, war, globalism, and the response to terrorism.

<img src="images/acts_per_year.png" width="525"/>

It can be seen that terrorism was on the rise in the 80's and 90's but started to trend down in the early 2000. Post 9/11 tensions began to rise and terrorism peaked in 2014. It can also be seen that bombings and armed assult were the two primary methods of attack.


<img src="images/suc_by_atk.png" width="525"/>
When the attack methods are explored, it can be seen Bombings and Armed Assults have the most success.

<img src="images/top_countries.png" width="525"/>
Post 9/11 the top countries affected by terrorism were Iraq, Pakistan, Afghanistan, India, and Columbia. Iraq is significantly higher than any other country in the database.

<img src="images/suc_by_co.png" width="525"/>
When Attacks are normalized, it can be seen that attacks in Iraq are the most effective. This demonstrates not just how unstable this country is, but also how it lacks the ability to fight the ongoing threat.


<img src="images/cas_per_atk.png" width="525"/>
Interestingly enough, attacks are becoming less deadly. This may indicate our ability to deal with the treat of terrorism is growing.

https://www.start.umd.edu/data-tools/global-terrorism-database-gtd

https://datacatalog.worldbank.org/dataset/global-data-set-education-quality
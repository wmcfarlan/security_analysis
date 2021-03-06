<a href="https://start.umd.edu/gtd/"><img src="images/logo.png" height=70%  width=70%  alt="Insights from Global Terrorist Dataset"></a>

# Global Terrorism Analysis
<br><br>

### An analysis of global terrorism and its interaction with female education rates.
___
__Abstract:__
I collected all known global acts of terrorism from the National Consortium for the Study of Terrorism and Responses to Terrorism from the years between 1970 and 2018. This data was analysed to find trends and insight. After conducting inital EDA, I have combined the National Consortium's dataset with global education data to further my analysis. My primary question: does the education of women affect number of terroristic events?


__Results:__
After conducting an analysis, I have concluded the education of females is directly correlated to acts of terrorism. This trend holds for both the percentage of women without education and for the percentage of women which have completed secondary school. These metrics were selected as they give a variety of standards for education.

___
# Background & Motivation
Terrorism is a constant security threat around the world. With more insight into how terrorism works, governments can make better decisions in dealing with present threats both in-boarders and abroad. While typical approaches to terrorism involve target hardening, counter-intelligence and military intervention, I wondered what role education played education. Specifically, the role of educating women.

My background is in psychotherapy, so I often look to more humanitarian based interventions to global conflict. If we can put a higher value to education and get reduced acts of terrorism, this would be a desireable approach. Education can be increased with policy changes and economic strategy.

___
# Hypothesis

H0: There is no statistically significant relationship between terrorism and the education of women

HA: There is a statistically significant relationship between terrorism and the education of women

Alpha Rate: 0.05


## Hypothesis Test

Spearman R was used due to the nonlinear distribution of education and terrorist acts per country. When log transformed, the distribution of data remained non-linear.

___
# Analysis methods

Two separate ```.csv``` files were used in data collection. The terrorist dataset pulled from START consists of over 200,000 different terrorist events from all over the world between 1970 and 2018. Educational statistics were pulled from World Bank. These statistics included 163 different countries and regions. Primary libraries used to analyze the data were ```pandas```, ```numpy``` and ```scipy```. To analyze the data, ```matplotlib```, and ```plotly``` were primarily used.

 
Due to the different designs of the datasets, many manipulations were required to merge and gain usable insight. Each presented their own challenges, however automated tools were designed to simplify the process within ```pipeline.py```.


___
# Terrorism and Education
How a country values and allocates education to women says a lot about the local politics, government structure and behaviors of a country. I combined terrorist dataset found on [http://gtd.terrorismdata.com](https://www.start.umd.edu/data-tools/global-terrorism-database-gtd) with world wide educational statistics found on [https://www.worldbank.org](https://datacatalog.worldbank.org/dataset/global-data-set-education-quality). Two two educational metrics I used were percent of women with no education and percent of women that have completed secondary education. These statistics are gathered globally in 5 year intervals from 1970 to 2010.

I selected these two metrics specifically because they give two different stringency levels for education. No education is a seemingly low bar, while global rates of women that have completed secondary education is a significant goal. When this data was combined with terrorist events, the below correlations were found.

<img src="images/edu_vs_atk.png" width="650"/>

Each dot is a countrie's mean education from 1970 to 2010 correlated with a contries mean acts of terrorism from 1970 to 2010. The leftmost plot shows the correlation in women that have completed secondary education and acts of terror. It can be seen with a regression line, there does appear to be a pattern.

The leftmost plot is percentage of women with no education and acts of terrorism. The regression line also demonstrates as education increases, terrorism decreases. However after plotting this data, I am wondering what the skew is and what an appropriate metric for conducting a hypothesis test would be. Below this is explored.

<img src="images/edu_vs_atk_dis.png" width="600"/>
It appears all education is right skewed. This indicates a non linear relationship and informs my selection of an appropriate correlational test. I select Spearman R for this reason.
 
* % women that have completed secondary education
* p-value: 0.0103
 
* % of women that have received no education
* p-value: 0.009
 
I can now reject my null hypothesis and can safely conclude education does affect rates of terrorism.


___
## Limitations
It is important to note correlation doesn't  equal causation. Terrorism by its very nature is an ourlier event and each organization involved in commiting acts of terror have different ideologies and motivations. Each country is distinct from one another and has their own cultural issues. It would be valuable to evaluate each country individually and do research on the socio-economic issues of each country to gain more insight.
___
# Insights into Terrorism: A Post 9/11 World
In order to trend terrorism, I focused on events after 9/11. The Twin Tower terrorist attack was a moment of global change, in terms of politics, war, globalism, and the response to terrorism.

<img src="images/acts_per_year.png" width="600"/>

* Terrorism was on the rise in the 80's and 90's
* Acts of Terrorism had a significant spike in 2014, this is when the US started to engage ISIS in Iraq
* Bombings and Armed Assault are the two primary terroristic threats


<img src="images/suc_by_atk.png" width="600"/>


* Bombings and Armed Assult are the most successful means of attack
* Dedicating security resources to track weapons and bomb parts may be a meanful approach to reducing these two threats

<img src="images/top_countries.png" width="600"/>

* Post 9/11 Iraq is the most contested country in the world by a significant margin 
* This may be attributed to the rise of ISIS


<img src="images/suc_by_co.png" width="600"/>

* Iraq is not equipped at dealing with terrorism
* This is the country to focus effects and resorces on

<img src="images/cas_per_atk.png" width="600"/>

* Terrorism is becoming less deadly with fewer killed and fewer injured
* This may indicate we are more capable at dealing with terrorism even with the rise of rates of terrorism

___
# Future Research
A more costom approach to understanding terrorism is needed. Each country is different and each terrorist group has a different ideology. This study was more of a top down study and does not grasp the sheer complexity of such events.
___

# Tech M&A prediction with patent data

The aim of the project is to set up a system to predict the possibility of a merger or acquisition of a tech startup. Based on the similarity of a startup's patents with the patents of other companies, one could predict whether or not this startup is an interesting target for other companies.

The results of this study are interesting for VC funds. This allows them to drastically reduce their potential targets, to focus on tech companies with a high  probability of being bought out in a M&A process, thus allowing VC funds to gain more premium and lose less time in the choice of their target.

Raw patent data is coming from : https://www.patentsview.org/

The pre-calculated similarity data comes from the database given by Ryan Whalen: https://github.com/ryanwhalen/patent_similarity_data

# Summary of code results
Of the last 100 startup M&A deals reported on Crunchbase at that time, 31 were between two companies each having at least 1 patent.

The idea now is to determine the similarity between the patents on both sides of the deals, the similarity between the purchaser's patents and those of the target. To do this, it is necessary to use the pre-established database with the similarity already calculated, or to determine the similarity between all the patents "by hand" using NLP processes. For a first approach, we will use the already calculated database, so we have to extract the good patents because the file is very heavy (20Go) and I can't put it in flash memories. For that, a simple method is to browse the JSon without putting it in the RAM (JSon stream), that increases the search time, but it works.

# a %9 relevance, HUGE
Out of 100 mergers, 31 are carried out between two companies each having at least one patent, and 9 are carried out between two companies having at least one patent sufficiently close. Out of this first sample of 100 mergers, we therefore have a model relevance for about 9% of the total mergers, which is huge. This would mean that 9% of the mergers and acquisitions notified on CrunchBase are relevant for the study. It's going to be fun (WORK IN PROGRESSS....).

def similarity_patents_betw_2_firme(firms):
    acquiree = firms[0]
    acquirer = firms[1]
    
    assignee_id_acquiree = assignee_1[assignee_1['organization'].str.contains(acquiree, regex=True, na=False)]['assignee_id'].iloc[0]
    assignee_id_acquirer = assignee_1[assignee_1['organization'].str.contains(acquirer, regex=True, na=False)]['assignee_id'].iloc[0]

    patents_acquiree = set(assignee_2[assignee_2['assignee_id']==assignee_id_acquiree]["patent_id"])
    patents_acquirer = set(assignee_2[assignee_2['assignee_id']==assignee_id_acquirer]["patent_id"])

    
    similarity_acquiree_dico = {}
    similarity_acquirer_dico = {}

    for sim in infile:
        json_load = json.loads(sim)
        if json_load[0] in patents_acquiree:
            similarity_acquiree_dico[json_load[0]] = json_load[1]
        if json_load[0] in patents_acquirer:
            similarity_acquirer_dico[json_load[0]] = json_load[1] 
        
    return(similarity_acquiree_dico,similarity_acquirer_dico)


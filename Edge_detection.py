def Edge_contact_detection(mdbname):
    All_instances=mdb.models[mdbname].rootAssembly.instances
    Instance_names=All_instances.keys()
    Instances_edges_list=[]
    for instance_name in Instance_names:
        edges_point_list=[]
        instance_vertices=mdb.models[mdbname].rootAssembly.instances[instance_name].vertices
        for vertice in instance_vertices:
            edge_point_list=[]
            for point in vertice.pointOn:
                edge_point_list.append(list(point))
            edges_point_list.append(edge_point_list)
        Instances_edges_list.append(edges_point_list)
    Instances_edges_squad=[]
    for i in Instances_edges_list:
        Instance_edges_squad=[]
        for j in range(len(i)-1):
            edge_squad_list=[i[j],i[j+1]]
            edge_squad_list.sort()
            Instance_edges_squad.append(edge_squad_list)
        edge_squad_list=[i[0],i[-1]]
        edge_squad_list.sort()
        Instance_edges_squad.append(edge_squad_list)
        Instances_edges_squad.append(Instance_edges_squad)
    print(Instances_edges_squad)
    num=0
    num_ins=0
    for i in range(len(Instances_edges_squad)):
        Ins=Instance_names[num_ins]
        num_ins+=1
        for j in range(i+1,len(Instances_edges_squad)):
            for k in Instances_edges_squad[i]:
                for l in Instances_edges_squad[j]:
                    if k==l:
                        a=0
                        b=0
                        c=0
                        for m in k:
                            a+=m[0][0]
                            b+=m[0][1]
                            c+=m[0][2]
                        pointOn=(a/2,b/2,c/2)
                        edges=mdb.models[mdbname].rootAssembly.instances[Ins].edges.findAt(pointOn)
                        highlight(edges)
                        num+=1
                        print('Edge coordinates',str(k))
    print('Contact detected in '+str(num)+' places')

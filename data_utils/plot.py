import matplotlib.pyplot as plt
import numpy as np
import os

def display_data_distribution(client_idcs, train_labels, num_classes, n_clients, args):
    # 展示不同client的不同label的数据分布，注意列表命名为clients
    plt.figure(figsize=(20, 6)) # 3
    label_distribution = [[] for _ in range(num_classes)]
    for c_id, idc in enumerate(client_idcs):
        for idx in idc:
            label_distribution[train_labels[idx]].append(c_id)
    
    plt.hist(label_distribution, stacked=True, 
             bins=np.arange(-0.5, n_clients + 1.5, 1),
            label=["Class {}".format(i) for i in range(num_classes)], rwidth=0.5)
    plt.xticks(np.arange(n_clients), ["Client %d" % c_id for c_id in range(n_clients)])
    plt.ylabel("Number of samples")
    plt.xlabel("Client ID")
    plt.legend()
    if args.pathological_split:
        dataset_split_method =  "Pathological"
    else:
        dataset_split_method = "Dirichlet"
    plt.title("Federated " + args.dataset + " Display(%s)" % dataset_split_method)
    plot_file = os.path.join(args.log_dir, "fed-" + args.dataset + "-display.png")
    plt.savefig(plot_file)
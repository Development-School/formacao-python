
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_data_science & usuarios_machine_learning)
# {56, 23}

print(usuarios_data_science - usuarios_machine_learning)
# {43, 15}

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
print(fez_ds_mas_nao_fez_ml)
{43, 15}

print(15 in fez_ds_mas_nao_fez_ml)
True

print(usuarios_data_science ^ usuarios_machine_learning)
# {42, 43, 13, 15}
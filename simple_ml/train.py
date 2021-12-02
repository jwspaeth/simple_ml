from hydra.utils import instantiate

from simple_ml.utils import setup_ml


def train(return_validation_result=True, **kwargs):
    data_dict, model, trainer = setup_ml(**kwargs)
    trainer.fit(model, **data_dict)

    if return_validation_result:
        return 0
from hydra.utils import instantiate

from simple_ml.utils import setup_ml, load_data


def test(**kwargs):
    data_dict, model, trainer = setup_ml(**kwargs)
    trainer.test(model, **data_dict)
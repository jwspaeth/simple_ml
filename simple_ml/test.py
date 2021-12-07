from hydra.utils import instantiate

from simple_ml.utils import setup_ml


def test(ckpt_path=None, **kwargs):
    data_dict, model, trainer = setup_ml(**kwargs)
    trainer.test(model, ckpt_path=ckpt_path, **data_dict)
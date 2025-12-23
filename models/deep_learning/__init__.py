# models/deep_learning/__init__.py
from .efficientnet_3d import EfficientNet3D
from .cnn_bilstm_attention import CNNBiLSTMAttention
from .temporal_gcn import TemporalGCN
from .vision_transformer import VisionTransformer

def get_model(model_name: str, config: dict):
    """
    Factory function to get model by name.
    
    Args:
        model_name: Name of the model
        config: Configuration dictionary
        
    Returns:
        model: Initialized model
    """
    models = {
        'efficientnet_3d': EfficientNet3D,
        'cnn_bilstm_attention': CNNBiLSTMAttention,
        'temporal_gcn': TemporalGCN,
        'vision_transformer': VisionTransformer
    }
    
    if model_name not in models:
        raise ValueError(f"Model {model_name} not found. Available: {list(models.keys())}")
    
    return models[model_name](config)

__all__ = [
    'EfficientNet3D',
    'CNNBiLSTMAttention',
    'TemporalGCN',
    'VisionTransformer',
    'get_model'
]

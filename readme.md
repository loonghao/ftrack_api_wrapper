ftrack_api_wrapper
==================


```python
from ftrack_api_wrapper import Session
ftrack_session = Session()
print ftrack_session.get_note_by_id('295bd9cc-55e5-11e8-bfc5-00e04c6819f3')

```

```python
from ftrack_api_wrapper.utils import create_thumbnail
create_thumbnail('pipelinernd_rnd-0000', "env_blackp-a", 'shd',"c:/thumb.png")
```
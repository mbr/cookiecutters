FROM {{base_image}}
LABEL Description="{{description}}"
MAINTAINER {{user_full_name}} <{{user_email}}

RUN apt-get update && apt-get install -y {{packages}}

CMD ['/bin/bash']

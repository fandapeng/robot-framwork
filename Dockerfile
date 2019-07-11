FROM python:2.7.15-alpine3.6
RUN mkdir /opt/app -p
WORKDIR /opt/app

# 拷贝代码
COPY . .

RUN sed -i 's#dl-cdn.alpinelinux.org#mirrors.aliyun.com#g' /etc/apk/repositories && \
	apk update && apk add dosfstools && apk add tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone
# 安装依赖项
RUN pip install -r requestments.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com && \
	python Library/update_library.py && \
	dos2unix /opt/app/entrypoint.sh && chmod +x /opt/app/entrypoint.sh

ENTRYPOINT ["/opt/app/entrypoint.sh"]
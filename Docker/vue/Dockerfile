FROM node:16.18.0 AS build
WORKDIR /frontend
COPY frontend .
ENV VUE_APP_SERVER http://170.64.136.159/api/
RUN npm install --legacy-peer-deps

FROM nginx:latest
COPY ./vue/nginx.conf /etc/nginx/conf.d/cs371.conf
COPY --from=build /frontend/dist /usr/share/nginx/html

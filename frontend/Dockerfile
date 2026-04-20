ARG NODE_BUILD_IMAGE=node:24-alpine
ARG NODE_RUNTIME_IMAGE=node:24-alpine

FROM ${NODE_BUILD_IMAGE} AS build

WORKDIR /app

COPY package*.json ./

RUN npm ci --legacy-peer-deps \
    && npm install --no-save --package-lock=false --legacy-peer-deps --no-audit --no-fund \
        pinia@3.0.4 vue-echarts@8.0.1 echarts@6.0.0

COPY . .

RUN npm run build

FROM ${NODE_RUNTIME_IMAGE} AS prod

WORKDIR /app

ENV NODE_ENV=production \
    HOST=0.0.0.0 \
    PORT=3000

COPY --from=build --chown=10001:10001 /app/.output /app/.output

USER 10001:10001

EXPOSE 3000

CMD [ "node", ".output/server/index.mjs" ]

'use strict';

const checkIdentity = async (data) => {
    const { application } = data

    const flagged = (application.name.indexOf('evil') !== -1)
    return { applicationId: application.id, flagged }
}

const commandHandlers = {
    'CHECK_IDENTITY': checkIdentity,
}

module.exports.handler = async (event) => {
    try {
        const isAPiGatewayRequest = event.requestContext && event.requestContext.apiId
        const params = typeof event.body === "string" ? JSON.parse(event.body) : event.body 
        const result = await commandHandlers[params.command](params.data)

        if (!isAPiGatewayRequest) return result

        const response = {
            statusCode: 200,
            body: JSON.stringify(result),
        };
        return response;
    }
    catch(ex) {
        console.error(ex)
        console.info('event', JSON.stringify(event))
    }
};

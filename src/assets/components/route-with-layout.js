import * as React from "react";
import { Route } from "react-router-dom";

const RouteWithLayout = (props) => {
    const { layout: Layout, component: Component, title, ...rest } = props;

    return (
        <Route
            {...rest}
            render={(matchProps) => (
                <Layout title={title}>
                    <Component {...matchProps} />
                </Layout>
            )}
        />
    );
};

export default RouteWithLayout;

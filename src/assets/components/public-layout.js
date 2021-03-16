import React from "react";

const PublicLayout = (props) => {
    const { children } = props;

    return (
        <>
            <div className="page-container">{React.cloneElement(children)}</div>
        </>
    );
};

export default PublicLayout;

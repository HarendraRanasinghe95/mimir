import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, withHandlers } from 'recompose';
import { detachFile } from 'actions';

import { isEmpty } from 'utils';

import ButtonCover from 'components/button/ButtonCover'

const enhance = compose(
    connect(
        null,
        dispatch => ({
            detachImage(imageId) {
                dispatch(detachFile(imageId))
            },
        }),
    ),
    withProps(props => ({
        label: 'Detach Image',
    })),
    withHandlers({
        onClick: props => event => {
            if (props.imageId) {
                props.detachImage(props.imageId);
            }
        }
    })
);

export default enhance(ButtonCover);
import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, withHandlers } from 'recompose';
import { attachFile } from 'actions';

import { isEmpty } from 'utils';

import ButtonCover from 'components/button/ButtonCover'

const enhance = compose(
    connect(
        null,
        dispatch => ({
            attachImage(imageId) {
                dispatch(attachFile(imageId))
            },
        }),
    ),
    withProps(props => ({
        label: 'Attach Image',
    })),
    withHandlers({
        onClick: props => event => {
            if (props.imageId) {
                props.attachImage(props.imageId);
            }
        }
    })
);

export default enhance(ButtonCover);
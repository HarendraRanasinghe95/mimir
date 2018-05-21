import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, withHandlers } from 'recompose';

import { isEmpty } from 'utils';
import { openModal } from 'actions';

import ButtonCover from 'components/button/ButtonCover'

const enhance = compose(
    connect(
        null,
        dispatch => ({
            openModal() {
                dispatch(openModal('manageModels'))
            },
        }),
    ),
    withProps(props => ({
        label: 'Manage Models',
    })),
    withHandlers({
        onClick: props => event => {
            props.openModal();
        }
    })
);

export default enhance(ButtonCover);
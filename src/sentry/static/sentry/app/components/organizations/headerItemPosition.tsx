import styled from 'react-emotion';

const HeaderItemPosition = styled('div')<{
  isSpacer?: boolean;
}>`
  display: flex;
  flex: 1;
  min-width: 0;
  height: 100%;

  ${p =>
    p.isSpacer &&
    `
    @media (max-width: ${p.theme.breakpoints[1]}) {
      display: none;
    }
  `}
`;

export default HeaderItemPosition;

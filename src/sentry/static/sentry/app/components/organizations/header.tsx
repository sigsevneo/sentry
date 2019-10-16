import styled from 'react-emotion';
import {Flex} from 'grid-emotion';

const Header = styled(Flex)`
  position: relative;
  width: 100%;
  height: 60px;

  border-bottom: 1px solid ${p => p.theme.borderDark};
  box-shadow: ${p => p.theme.dropShadowLight};
  z-index: ${p => p.theme.zIndex.globalSelectionHeader};

  background: #fff;
  font-size: ${p => p.theme.fontSizeExtraLarge};
`;

export default Header;

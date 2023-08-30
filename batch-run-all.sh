tamarin-prover-release +RTS -N10 -RTS --output=proofs.spthy \
  --prove=TLSKeyShareRecursion \
  --prove=TLSKeyLeakRecursion \
  --prove=WrongCAKeyUseImpliesCompromise \
  --prove=CanObtainRootKey \
  --prove=VerifiedAuthorityOrigin \
  --prove=AuthenticEmblem \
  --prove=CanDisupte \
  --prove=CAAccountability \
  --prove=AuthorityAccountability \
  --prove=PPAccountability \
  --prove=RootKeyUse \
  adem.spthy > proofs.log 2>&1 &
